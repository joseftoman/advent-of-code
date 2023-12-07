#!/usr/bin/perl
use warnings; use strict;

my %match = (
  children => 3,
  cats => 7,
  samoyeds => 2,
  pomeranians => 3,
  akitas => 0,
  vizslas => 0,
  goldfish => 5,
  trees => 3,
  cars => 2,
  perfumes => 1,
);

while (my $sue = <STDIN>) {
  my ($num, $info) = $sue =~ m/^Sue (\d+): (.*)/;
  map {
    m/(.*): (\d+)/;
    next if $match{$1} != $2;
  } split /, /, $info;
  print "$num\n";
}
