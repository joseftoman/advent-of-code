#!/usr/bin/perl
use warnings; use strict;

my @g;
for my $x (0..999) {
  for my $y (0..999) {
    $g[$x][$y] = 0;
  }
}

map {
  my ($c, $x1, $y1, $x2, $y2) = m/^(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)/;

  for my $x ($x1..$x2) {
    for my $y ($y1..$y2) {
      if ($c eq 'turn on') {
        $g[$x][$y] += 1;
      } elsif ($c eq 'turn off') {
        $g[$x][$y] -= 1 unless $g[$x][$y] == 0;
      } else {
        $g[$x][$y] += 2;
      }
    }
  }
} <STDIN>;

my $sum = 0;
for my $x (0..999) {
  for my $y (0..999) {
    $sum += $g[$x][$y];
  }
}

print "$sum\n";
