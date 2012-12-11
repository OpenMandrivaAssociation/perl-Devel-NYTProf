%define upstream_name  	    Devel-NYTProf
%define upstream_version 4.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3
Summary:    Powerful feature-rich perl source code profiler
Group:      Development/Perl
License:    Artistic
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More) >= 0.88
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
%setup -q -n %{upstream_name}-%{upstream_version} 

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



%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 4.60.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 4.60.0-2
+ Revision: 681402
- mass rebuild

* Thu Dec 02 2010 Guillaume Rousse <guillomovitch@mandriva.org> 4.60.0-1mdv2011.0
+ Revision: 604717
- update to new version 4.06
- update to new version 4.05

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 4.40.0-2mdv2011.0
+ Revision: 555249
- rebuild

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 4.40.0-1mdv2011.0
+ Revision: 553125
- update to 4.04

* Wed Mar 17 2010 Jérôme Quelin <jquelin@mandriva.org> 3.110.0-1mdv2010.1
+ Revision: 523439
- update to 3.11

* Fri Mar 05 2010 Jérôme Quelin <jquelin@mandriva.org> 3.20.0-1mdv2010.1
+ Revision: 514401
- update to 3.02

* Wed Dec 30 2009 Jérôme Quelin <jquelin@mandriva.org> 3.10.0-1mdv2010.1
+ Revision: 483901
- update to 3.01

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.100.0-1mdv2010.0
+ Revision: 389935
- new version

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.09-1mdv2010.0
+ Revision: 370051
- update to new version 2.09

* Mon Feb 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.08-1mdv2009.1
+ Revision: 340754
- update to new version 2.08

* Fri Nov 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.07-1mdv2009.1
+ Revision: 300700
- new version
  spec rewrite

* Thu Oct 16 2008 Thierry Vignaud <tv@mandriva.org> 2.05-1mdv2009.1
+ Revision: 294255
- BuildRequires:  perl-devel
- import perl-Devel-NYTProf


* Thu Oct 09 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.05-1mdv2009.1
- Initial build.
