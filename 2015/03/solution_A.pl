#!/usr/bin/perl
use warnings; use strict;

my $x = 0;
my $y = 0;
my %h = ("${x}x${y}" => 1);
my %d = (
  '>' => [ 1, 0],
  '<' => [-1, 0],
  '^' => [ 0, 1],
  'v' => [ 0,-1],
);

for my $c (split '', <STDIN>) {
  $x += $d{$c}->[0];
  $y += $d{$c}->[1];
  $h{"${x}x${y}"} = 1;
}

print scalar(keys %h), "\n";
