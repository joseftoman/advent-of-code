#!/usr/bin/perl
use warnings; use strict;

my %repl;
my $max_r = 0;
my %set = ('e' => 1);
my $gen = 0;
my $ok = 0;

while (my ($l, $r) = <STDIN> =~ m/^(\w+) => (\w+)$/) {
  $repl{$l} //= [];
  push @{$repl{$l}}, $r;
  $max_r = length($r) if length($r) > $max_r;
}
my $goal = <STDIN>;
chomp $goal;

while (not exists $set{substr($goal, $ok)}) {
  my @q = keys %set;
  %set = ();
  $gen++;
  my $min_l;
  
  for my $m (@q) {
    my ($use, $copy);
    if (length($m) > $max_r) {
      $use = substr($m, 0, $max_r);
      $copy = substr($m, $max_r);
    } else {
      $use = $m;
      $copy = '';
    }

    while (my ($left, $list) = each %repl) {
      my @parts = split /$left/, "_${use}_";
      next unless scalar(@parts) > 1;

      for (my $i = 0; $i < $#parts; $i++) {
        for my $s (@$list) {
          my $new = substr(join($left, @parts[0..$i]).$s.join($left, @parts[$i+1..$#parts]), 1, -1).$copy;
          $set{$new} = 1;
          my $l = length($new);
          $min_l = $l if not(defined $min_l) || $min_l > $l;
        }
      }
    }
  }

  my $sum = 0;
  $sum += length($_) for keys %set;
  printf("GEN %3d: size = %d, length = %.2f\n", $gen, scalar(keys %set), $sum / scalar(keys %set));

  if ($min_l > $max_r) {
    my $want = $min_l - $max_r;
    my @select;
    for my $m (keys %set) {
      push @select, substr($m, $want) if substr($m, 0, $want) eq substr($goal, $ok, $want);
    }

    unless (@select) {
      print "Dead end\n";
      exit;
    }
    $ok += $want;

    my $sum = 0;
    $sum += length($_) for @select;
    printf(" OK %3d: size = %d, length = %.2f\n\n", $ok, scalar(@select), $sum / scalar(@select));
    %set = map { $_ => 1 } @select;
  }
}

print "$gen\n";

sub prefix_length {
  my ($s, $min) = @_;
  my $len = length($s) - $max_r;
  return 0 unless $len >= $min and substr($s, 0, $min) eq substr($goal, 0, $min);
  my $pos = $min;

  while ($len > $pos and substr($s, $pos, 1) eq substr($goal, $pos, 1)) {
    $pos++;
  }

  return $pos;
}
