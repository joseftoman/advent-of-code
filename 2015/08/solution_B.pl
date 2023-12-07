#!/usr/bin/perl
use warnings; use strict;
use Data::Dump;

my $total = 0;

map {
  chomp;
  $total -= length;
  $total += length(Data::Dump::pp($_));
} <STDIN>;

print "$total\n";
