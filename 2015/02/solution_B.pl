#!/usr/bin/perl
use warnings; use strict;
use List::Util 'min';

my $sum = 0;
map $sum += ribbon_for_a_box($_), <STDIN>;
print "$sum\n";

sub ribbon_for_a_box {
  my $spec = shift;
  my $total = 0;

  my @a = sort { $a <=> $b } split 'x', $spec;
  return 2*$a[0] + 2*$a[1] + $a[0]*$a[1]*$a[2];
}
