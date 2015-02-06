%define upstream_name    Debug-ShowStuff
%define upstream_version 1.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A collection of handy debugging routines for displaying
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Debug/Debug-ShowStuff-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(String::Util)
BuildRequires:	perl(Tie::IxHash)
BuildArch:	noarch

%description
'Debug::ShowStuff' grew dynamically from my needs in debugging code. I
found myself doing the same tasks over and over... displaying the keys and
values in a hash, displaying the elements in an array, displaying the
output of STDERR in a web page, etc. 'Debug::ShowStuff' began as two or
three of my favorite routines and grew as I added to that collection.
Finally I decided to publish these tools in the hope that other Perl
hackers will find them useful.

'Debug::ShowStuff' is intended for debugging, not for production work. I
would discourage anyone from using 'Debug::ShowStuff' in
ready-for-primetime code. 'Debug::ShowStuff' is only for quick-n-dirty
displays of variable values in order to debug your code.

These functions display values the way I personally like them displayed.
Your preferences may be different. I encourage you to modify
'Debug::ShowStuff' to suit your own needs.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.130.0-3mdv2011.0
+ Revision: 657775
- rebuild for updated spec-helper
- rebuild for updated spec-helper

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.130.0-1mdv2011.0
+ Revision: 612076
- update to new version 1.13

* Sun Nov 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.110.0-1mdv2011.0
+ Revision: 597580
- update to new version 1.11

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2011.0
+ Revision: 596656
- import perl-Debug-ShowStuff


