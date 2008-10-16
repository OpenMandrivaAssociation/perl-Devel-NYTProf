%define pkgname    Devel-NYTProf
%define filelist %{pkgname}-%{version}-filelist
%define NVR %{pkgname}-%{version}-%{release}
Summary:       Devel-NYTProf - Powerful feature-rich perl source code profiler
Name:          perl-Devel-NYTProf
Version:       2.05
Release:       %mkrel 1
Group:         Development/Perl
License:       Artistic
Url:           http://www.cpan.org
BuildRoot:     %{_tmppath}/%{name}-%{version}-%(id -u -n)
#BuildArch:     i586
Source:        http://search.cpan.org/CPAN/authors/id/T/TI/TIMB/%{pkgname}-%{version}.tar.gz
%description
# profile code and write database to ./nytprof.out
perl -d:NYTProf some_perl.pl
# convert database into a set of html files, e.g., ./nytprof/index.html
nytprofhtml
# or into comma seperated files, e.g., ./nytprof/*.csv
nytprofcsv

%prep
%setup -q -n Devel-NYTProf-2.05 

%build
CFLAGS="$RPM_OPT_FLAGS"
perl Makefile.PL INSTALLDIRS=vendor
%make 
%make test

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%{makeinstall}  PREFIX=$RPM_BUILD_ROOT%{_prefix} DESTDIR=$RPM_BUILD_ROOT
#%makeinstall_std
find $RPM_BUILD_ROOT -name "perllocal.pod" \
-o -name ".packlist"                    \
-o -name "*.bs"                         \
|xargs -i rm -f {}
find $RPM_BUILD_ROOT%{_prefix} -type d -depth -exec rmdir {} \; 2>/dev/null

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc bin/nytprofhtml Changes INSTALL README
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorarch}/Devel
%{perl_vendorarch}/auto/*

