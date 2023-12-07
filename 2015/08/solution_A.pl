#!/usr/bin/perl
use warnings; use strict;

my $total = 0;

map {
  chomp;
  $total += length;
  $total -= length(eval);
} <STDIN>;

print "$total\n";
