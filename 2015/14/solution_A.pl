#!/usr/bin/perl
use warnings; use strict;
use List::Util 'min';

my $limit = 2503;
my $max = 0;

map {
  m/^(\S+) can fly (\d+) km\/s for (\d+) seconds?, but then must rest for (\d+) seconds?\.$/;
  my $d = 0;
  $d += int($limit / ($3 + $4)) * $3 * $2;
  $d += min($limit % ($3 + $4), $3) * $2;
  $max = $d if $d > $max;
  #print "$1: $d km\n";
} <STDIN>;

print "MAX = $max km\n";
