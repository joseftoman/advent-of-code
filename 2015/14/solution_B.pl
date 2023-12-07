#!/usr/bin/perl
use warnings; use strict;
use List::Util 'min';

my $limit = 2503;
my @r;
for my $line (<STDIN>) {
  $line =~ m/^(\S+) can fly (\d+) km\/s for (\d+) seconds?, but then must rest for (\d+) seconds?\.$/;
  push @r, {
    name => $1,
    speed => $2,
    fly => $3,
    rest => $4,
    points => 0,
    distance => 0,
    is_flying => 1,
    left => $3,
  };
}

my $max;
for (1..$limit) {
  $max = 0;
  move($_) for @r;
  do {
    $_->{points}++ if $_->{distance} == $max;
  } for @r;
}

$max = 0;
for my $r (@r) {
  $max = $r->{points} if $max < $r->{points};
  #print "$r->{name}: $r->{distance} km ($r->{points})\n";
}
print "MAX = $max points\n";

sub move {
  my $r = shift;
  $r->{distance} += $r->{speed} if $r->{is_flying};
  $r->{left}--;
  unless ($r->{left}) {
    $r->{left} = $r->{$r->{is_flying} ? 'rest' : 'fly'};
    $r->{is_flying} = ($r->{is_flying} + 1) % 2;
  }
  $max = $r->{distance} if $max < $r->{distance};
}
