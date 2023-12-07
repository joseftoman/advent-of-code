#!/usr/bin/perl
use warnings; use strict;

die "usage: solution.pl NO < input\n" unless defined $ARGV[0];
my $s = <STDIN>;
chomp $s;

for (1..$ARGV[0]) {
  next_step();
  #print "$s\n";
}
print length($s), "\n";

sub next_step {
  my @chars = split '', $s;
  $s = '';
  my $c = shift @chars;
  my $i = 1;

  while (@chars) {
    my $n = shift @chars;

    if ($c eq $n) {
      $i++;
    } else {
      $s .= "$i$c";
      $c = $n;
      $i = 1;
    }
  }

  $s .= "$i$c";
}
