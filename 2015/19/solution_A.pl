#!/usr/bin/perl
use warnings; use strict;

my %repl;
my %res;
my $m;

while (my ($l, $r) = <STDIN> =~ m/^(\w+) => (\w+)$/) {
  $repl{$l} //= [];
  push @{$repl{$l}}, $r;
}
$m = <STDIN>;
chomp $m;
$m = "_${m}_";

while (my ($left, $list) = each %repl) {
  my @parts = split /$left/, $m;
  for (my $i = 0; $i < $#parts; $i++) {
    for my $s (@$list) {
      my $new = join($left, @parts[0..$i]).$s.join($left, @parts[$i+1..$#parts]);
      $res{$new} = 1;
    }
  }
}

print scalar(keys %res), "\n";
