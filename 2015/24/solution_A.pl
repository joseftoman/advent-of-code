#!/usr/bin/perl
use warnings; use strict;
use Algorithm::Combinatorics;

my @weights = map { chomp; $_ } <STDIN>;
my $sum = 0;
$sum += $_ for @weights;

my $min = knapsack($sum / 3, \@weights);
my $best;

do {
  $best = get_best($min, $sum / 3, \@weights);
  $min++;
} while not defined $best->[0];

print $best->[0], "\n";
print join(" ", sort { $a <=> $b } @{$best->[1]}), "\n";

sub knapsack {
  my ($goal, $items) = @_;
  my @a = (undef) x ($goal+1);
  $a[0] = 0;

  for my $w (@$items) {
    for (my $i = $#a - $w; $i >= 0; $i--) {
      next unless defined $a[$i];
      $a[$i + $w] = $a[$i] + 1 if not(defined $a[$i + $w]) or $a[$i + $w] > $a[$i] + 1;
    }
  }

  return $a[$goal];
}

sub get_best {
  my ($size, $goal, $items) = @_;
  my $min = undef;
  my $min_set;

  my $iter = Algorithm::Combinatorics::combinations($items, $size);
  while (my $set = $iter->next()) {
    my $score = 0;
    $score += $_ for @$set;
    next if $score != $goal;

    my %map = map { $_ => 1 } @$set;
    my @diff = grep { not exists $map{$_} } @$items;
    next unless defined knapsack($goal, \@diff);

    $score = 1;
    $score *= $_ for @$set;
    if (not(defined $min) or $score < $min) {
      $min = $score;
      $min_set = $set;
    }
  }

  return [ $min, $min_set ];
}
