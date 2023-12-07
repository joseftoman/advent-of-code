#!/usr/bin/perl
use warnings; use strict;
use Heap::Fibonacci::Fast;
use Clone 'clone';
use List::Util 'max';
use Data::Dump;

my ($hp_boss) = <STDIN> =~ m/^Hit Points: (\d+)/;
my ($damage_boss) = <STDIN> =~ m/^Damage: (\d+)/;

my $spell = {
  missile => 53,
  drain => 73,
  shield => 113,
  poison => 173,
  recharge => 229,
};

my $init = {
  self => [ 50, 0, 500 ], # HP, Armor, Mana
  boss => [ $hp_boss, $damage_boss ],
  effects => {},
  mana => 0,
  spell => undef,
  prev => undef,
};

my @log = ($init);
my $heap = Heap::Fibonacci::Fast->new();
for my $s (keys %$spell) {
  $heap->key_insert($spell->{$s}, [0, $s]) if $spell->{$s} <= $init->{self}->[2];
}

while (my $item = $heap->extract_top()) {
  my $state = clone $log[$item->[0]];
  #print "FROM:\n"; dd $state; print "SPELL: $item->[1]\n";
  $state->{prev} = $item->[0];
  cast_spell($state, $item->[1]);
  #dd $state;

  $state->{self}->[1] = 0; # Armor
  apply_effect($state);
  #print "EFFECTS:\n"; dd $state;

  $state->{self}->[0] -= max(1, $state->{boss}->[1] - $state->{self}->[1]);
  #print "BOSS:\n"; dd $state;

  $state->{self}->[0]--;
  next unless $state->{self}->[0] > 0; # Death

  apply_effect($state);
  #print "EFFECTS:\n"; dd $state;

  my @avail = grep { $spell->{$_} <= $state->{self}->[2] and not exists $state->{effects}->{$_} } keys %$spell;
  next unless @avail; # Not enough mana

  push @log, $state;
  #print "NEXT: ", join(', ', @avail), "\n\n";
  $heap->key_insert($state->{mana} + $spell->{$_}, [$#log, $_]) for @avail;
}

print "Boss can not be defeated\n";

sub cast_spell {
  my ($state, $name) = @_;
  $state->{spell} = $name;
  $state->{self}->[2] -= $spell->{$name};
  $state->{mana} += $spell->{$name};

  if ($name eq 'missile') {
    $state->{boss}->[0] -= 4;
  } elsif ($name eq 'drain') {
    $state->{self}->[0] += 2;
    $state->{boss}->[0] -= 2;
  } elsif ($name eq 'shield') {
    $state->{effects}->{shield} = 6;
  } elsif ($name eq 'poison') {
    $state->{effects}->{poison} = 6;
  } elsif ($name eq 'recharge') {
    $state->{effects}->{recharge} = 5;
  }

  finish($state) if $state->{boss}->[0] <= 0;
}

sub apply_effect {
  my $state = shift;
  my @names = keys %{$state->{effects}};

  for my $s (@names) {
    if ($s eq 'shield') {
      $state->{self}->[1] = 7;
    } elsif ($s eq 'poison') {
      $state->{boss}->[0] -= 3;
    } elsif ($s eq 'recharge') {
      $state->{self}->[2] += 101;
    }
    if ($state->{effects}->{$s} == 1) {
      delete $state->{effects}->{$s};
    } else {
      $state->{effects}->{$s}--;
    }
  }

  finish($state) if $state->{boss}->[0] <= 0;
}

sub finish {
  my $state = shift;
  my @path = ($state);
  while (defined $path[0]->{prev}) {
    unshift @path, $log[$path[0]->{prev}];
  }
  print join("\n", map $_->{spell}, @path[1..$#path]), "\n";
  dd $state;
  print "\n$state->{mana}\n";
  exit;
}
