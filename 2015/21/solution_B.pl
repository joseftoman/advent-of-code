#!/usr/bin/perl
use warnings; use strict;
use List::Util 'max';
use POSIX 'ceil';

my $max;
my $max_set;

my ($hp_boss) = <STDIN> =~ m/^Hit Points: (\d+)/;
my ($damage_boss) = <STDIN> =~ m/^Damage: (\d+)/;
my ($defense_boss) = <STDIN> =~ m/^Armor: (\d+)/;

my $hp = 100;
my $weapon = [
  [  8, 4, 0, 'Dagger' ],
  [ 10, 5, 0, 'Shortsword' ],
  [ 25, 6, 0, 'Warhammer' ],
  [ 40, 7, 0, 'Longsword' ],
  [ 74, 8, 0, 'Greataxe' ],
];
my $armor = [
  [   0, 0, 0, 'none' ],
  [  13, 0, 1, 'Leather' ],
  [  31, 0, 2, 'Chainmail' ],
  [  53, 0, 3, 'Splintmail' ],
  [  75, 0, 4, 'Bandedmail' ],
  [ 102, 0, 5, 'Platemail' ],
];
my $ring = [
  [  25, 1, 0, 'Damage +1' ],
  [  50, 2, 0, 'Damage +2' ],
  [ 100, 3, 0, 'Damage +3' ],
  [  20, 0, 1, 'Defense +1' ],
  [  40, 0, 2, 'Defense +2' ],
  [  80, 0, 3, 'Defense +3' ],
];

for my $w (@$weapon) {
  for my $a (@$armor) {
    fight([$w, $a]);
    
    for (my $r1 = 0; $r1 <= $#$ring; $r1++) {
      fight([$w, $a, $ring->[$r1]]);

      for (my $r2 = $r1 + 1; $r2 <= $#$ring; $r2++) {
        fight([$w, $a, $ring->[$r1], $ring->[$r2]]);
      }
    }
  }
}

print "$max\n";
print join("\n", map $_->[3], @$max_set), "\n";

sub fight {
  my $set = shift;
  my ($price, $damage, $defense) = (0, 0, 0);
  for my $item (@$set) {
    $price += $item->[0];
    $damage += $item->[1];
    $defense += $item->[2];
  }

  my $deal = max($damage - $defense_boss, 1);
  my $receive = max($damage_boss - $defense, 1);
  my $need = ceil($hp_boss / $deal);
  return if ($need - 1) * $receive < $hp;

  if (not(defined $max) || $price > $max) {
    $max = $price;
    $max_set = $set;
  }
}
