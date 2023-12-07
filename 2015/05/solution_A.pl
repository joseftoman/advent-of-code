#!/usr/bin/perl
use warnings; use strict;

my $no = 0;
map $no += naughty_or_nice($_), <STDIN>;
print "$no\n";

sub naughty_or_nice {
  my $s = shift;
  chomp $s;

  for my $a (qw/ab cd pq xy/) {
    return 0 if index($s, $a) >= 0;
  }

  my @c = $s =~ m/([aeiou])/g;
  return 0 if scalar(@c) < 3;

  @c = split '', $s;
  for (my $i = 1; $i <= $#c; $i++) {
    return 1 if $c[$i] eq $c[$i-1];
  }
  return 0;
}
