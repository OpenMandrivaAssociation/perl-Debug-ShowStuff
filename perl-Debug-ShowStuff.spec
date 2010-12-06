%define upstream_name    Debug-ShowStuff
%define upstream_version 1.13

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A collection of handy debugging routines for displaying
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Debug/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Tie::IxHash)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%perl_vendorlib/*


