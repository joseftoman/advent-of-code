#!/usr/bin/perl
use warnings; use strict;

my @pos = (
  [0, 0],
  [0, 0],
);
my $s = 0;
my %h = ("0x0" => 1);
my %d = (
  '>' => [ 1, 0],
  '<' => [-1, 0],
  '^' => [ 0, 1],
  'v' => [ 0,-1],
);

for my $c (split '', <STDIN>) {
  $pos[$s][0] += $d{$c}->[0];
  $pos[$s][1] += $d{$c}->[1];
  $h{"$pos[$s][0]x$pos[$s][1]"} = 1;
  $s = ($s+1) % 2;
}

print scalar(keys %h), "\n";
