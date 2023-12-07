#!/usr/bin/perl
use warnings; use strict;

my $goal = $ARGV[0] or die "The goal is not set.\n";
my @c = map { chomp; $_ } <STDIN>;
my @mask = (0) x ($#c+1);
my $min = $#c + 1;
my $no = 0;
iterate(0);
print "$no ($min)\n";

sub iterate {
  my $pos = shift;
  $mask[$pos] = 0;
  $pos == $#mask ? evaluate() : iterate($pos+1);
  $mask[$pos] = 1;
  $pos == $#mask ? evaluate() : iterate($pos+1);
}

sub evaluate {
  my $sum = 0;
  my $amount = 0;
  for (my $i = 0; $i <= $#mask; $i++) {
    if ($mask[$i]) {
      $sum += $c[$i];
      $amount++;
    }
  }
  #print join(' ', @mask), " -> $sum\n";
  if ($sum == $goal) {
    if ($amount == $min) {
      $no++;
    } elsif ($amount < $min) {
      $min = $amount;
      $no = 1;
    }
  }
}
