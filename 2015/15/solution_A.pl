#!/usr/bin/perl
use warnings; use strict;
my @in;
my @o;
my @props = qw/capacity durability flavor texture/;

while (my $line = <STDIN>) {
  my ($name, $info) = split /: /, $line;
  push @in, { map { m/(.*) (-?\d+)/ } split /, /, $info };
  push @o, $name;
}

my $max = 0;
my @m;

iterate(0, 100, (0) x ($#in-1));
print "$max\n";
print map { "$o[$_] x $m[$_]\n" } (0..$#in);

sub iterate {
  my ($pos, @v) = @_;
  evaluate(@v);
  return if $pos == $#in;
  while ($v[$pos]) {
    $v[$pos]--;
    $v[$pos+1]++;
    iterate($pos+1, @v);
  }
}

sub evaluate {
  my @v = @_;
  my %sums = map { $_ => 0 } @props;
  for (my $i = 0; $i <= $#v; $i++) {
    $sums{$_} += $v[$i] * $in[$i]->{$_} for @props;
  }

  my $t = 1;
  $t *= $sums{$_} < 0 ? 0 : $sums{$_} for @props;
  if ($t > $max) {
    $max = $t;
    @m = @v;
  }
}
