#!/usr/bin/perl
use warnings; use strict;
use List::Util 'min';

my $sum = 0;
map $sum += wrapping_paper_for_a_box($_), <STDIN>;
print "$sum\n";

sub wrapping_paper_for_a_box {
  my $spec = shift;
  my $total = 0;

  my ($a, $b, $c) = split 'x', $spec;
  my @a = ($a*$b, $a*$c, $b*$c);
  my $min = min(@a);
  map $total += $_ * 2, @a;

  return $total + $min;
}
