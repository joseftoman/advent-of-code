#!/usr/bin/perl
use warnings; use strict;

my $no = 0;
map $no += naughty_or_nice($_), <STDIN>;
print "$no\n";

sub naughty_or_nice {
  my $s = shift;
  chomp $s;
  my $p = 0;

  my @c = split '', $s;

  P1:
  for (my $i = 2; $i < $#c; $i++) {
    for (my $j = 0; $j < $i - 1; $j++) {
      if ($c[$i] eq $c[$j] and $c[$i+1] eq $c[$j+1]) {
        $p++;
        last P1;
      }
    }
  }

  for (my $i = 2; $i <= $#c; $i++) {
    if ($c[$i] eq $c[$i-2]) {
      $p++;
      last;
    }
  }

  return $p == 2 ? 1 : 0;
}
