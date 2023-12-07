#!/usr/bin/perl
use warnings; use strict;

my @a = map ord($_) - 97, split '', <STDIN>;
iterate();
iterate() while not test();
print join('', map chr($_ + 97), @a), "\n";

sub iterate {
  my $i = $#a;
  my $c = 0;

  do {
    $a[$i]++;
    $c = 0;
    if ($a[$i] == 26) {
      $a[$i] = 0;
      $c = 1;
    }
    $i--;
    $c = 0 if $i < 0;
  } while ($c);
}

sub test {
  # i, l, o
  return 0 if grep { $_ == 8 or $_ == 11 or $_ == 14 } @a;

  my $ok = 0;
  my $i;
  for ($i = 2; $i <= $#a; $i++) {
    if ($a[$i-2] == $a[$i-1] - 1 and $a[$i-1] == $a[$i] - 1) {
      $ok = 1;
      last;
    }
  }
  return 0 unless $ok;

  $ok = 0;
  my $x = 26;
  my %h;
  for ($i = 0; $i <= $#a; $i++) {
    if ($a[$i] == $x) {
      $ok++;
      $h{$x} = 1;
      $x = 26;
    } else {
      $x = exists $h{$a[$i]} ? 26 : $a[$i]
    }
  }

  return $ok < 2 ? 0 : 1;
}
