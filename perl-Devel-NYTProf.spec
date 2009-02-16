%define module    Devel-NYTProf
%define version   2.08
%define release   %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
Summary:    Powerful feature-rich perl source code profiler
Group:      Development/Perl
License:    Artistic
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Devel/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRoot:     %{_tmppath}/%{name}-%{version}

%description
Devel::NYTProf is a powerful feature-rich perl source code profiler.

  * Performs per-line statement profiling for fine detail
  * Performs per-subroutine statement profiling for overview
  * Performs per-block statement profiling (the first profiler to do so)
  * Accounts correctly for time spent after calls return
  * Performs inclusive and exclusive timing of subroutines
  * Subroutine times are per calling location (a powerful feature)
  * Can profile compile-time activity, just run-time, or just END time
  * Uses novel techniques for efficient profiling
  * Sub-microsecond (100ns) resolution on systems with clock_gettime()
  * Very fast - the fastest statement and subroutine profilers for perl
  * Handles applications that fork, with no performance cost
  * Immune from noise caused by profiling overheads and I/O
  * Program being profiled can stop/start the profiler
  * Generates richly annotated and cross-linked html reports
  * Trivial to use with mod_perl - add one line to httpd.conf
  * Includes an extensive test suite
  * Tested on very large codebases

NYTProf is effectively two profilers in one: a statement profiler, and a
subroutine profiler.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%optflags"

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc bin/nytprofhtml Changes INSTALL README
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorarch}/Devel
%{perl_vendorarch}/auto/*

