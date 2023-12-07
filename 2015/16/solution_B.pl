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
    if ($1 eq 'cats' || $1 eq 'trees') {
      next if $2 <= $match{$1};
    } elsif ($1 eq 'pomeranians' || $1 eq 'goldfish') {
      next if $2 >= $match{$1};
    } else {
      next if $2 != $match{$1};
    }
  } split /, /, $info;
  print "$num\n";
}
