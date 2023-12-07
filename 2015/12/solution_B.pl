#!/usr/bin/perl
use warnings; use strict;
use JSON::XS;
my $data = decode_json <STDIN>;
my $sum = 0;
process($data);
print "$sum\n";

sub process {
  my $d = shift;
  my $t = ref($d) // '';
  if ($t eq 'ARRAY') {
    process($_) for @$d;
  } elsif ($t eq 'HASH') {
    unless (grep { $_ eq 'red' } values %$d) {
      process($_) for values %$d;
    }
  } elsif ($d =~ m/^-?\d+$/) {
    $sum += $d;
  }
}
