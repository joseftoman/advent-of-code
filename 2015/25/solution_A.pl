#!/usr/bin/perl
use warnings; use strict;

my ($row, $col) = <STDIN> =~ m/row (\d+), column (\d+)/;
my $pos = get_pos($row, $col);
my $code = 20151125;
$code = ($code * 252533) % 33554393 for 2..$pos;
print "$code\n";

sub get_pos {
  my ($row, $col) = @_;
  my $d = $row + $col - 2;
  my $pos = $d * ($d + 1) / 2 + $col;
  return $pos;
}
