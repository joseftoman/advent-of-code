#!/usr/bin/perl
use warnings; use strict;

my %p;
my %c;
my $max;
my $circle = [];
my $f;

for (<STDIN>) {
  m/^(\S+) would (gain|lose) (\d+) .* (\S+)\.$/;
  my $no = $3 * ($2 eq 'lose' ? -1 : 1);
  $p{$1} = 1;
  $p{$4} = 1;
  $c{$1}{$4} //= 0;
  $c{$4}{$1} //= 0;
  $c{$1}{$4} += $no;
  $c{$4}{$1} += $no;
  $f //= $1;
}

delete $p{$f};
solve([$f], \%p);
print join(' -> ', @$circle), " = $max\n";

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
      if (not defined $max or $d > $max) {
        @$circle = @$v;
        $max = $d;
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
    $sum += $c{$o->[$i-1]}{$o->[$i]};
  }
  $sum += $c{$o->[0]}{$o->[$#$o]};

  #print join(' <-> ', @$o), " = $sum\n";
  return $sum;
}
