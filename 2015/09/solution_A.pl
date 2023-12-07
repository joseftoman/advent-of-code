#!/usr/bin/perl
use warnings; use strict;

my %c;
my %d;
my $min;
my $path = [];

for (<STDIN>) {
  m/^(\S+) to (\S+) = (\d+)$/;
  $c{$1} = 1;
  $c{$2} = 1;
  $d{$1}{$2} = $3;
  $d{$2}{$1} = $3;
}

solve([], \%c);
print join(' -> ', @$path), " = $min\n";

sub solve {
  my ($v, $a) = @_;
  my %avail = %$a;
  my @order = keys %avail;

  for my $k (@order) {
    push @$v, $k;
    delete $avail{$k};

    if (%avail) {
      solve($v, \%avail);
    } else {
      my $d = distance($v);
      if (not defined $min or $d < $min) {
        @$path = @$v;
        $min = $d;
      }
    }

    $avail{$k} = 1;
    pop @$v;
  }

}

sub distance {
  my $o = shift;
  my $sum = 0;

  for (my $i = 1; $i <= $#$o; $i++) {
    $sum += $d{$o->[$i-1]}{$o->[$i]};
  }

  #print join(' -> ', @$o), " = $sum\n";
  return $sum;
}
