Name:       gzip
Summary:    The GNU data compression program
Version:    1.9
Release:    1
Group:      Applications/File
License:    GPLv3 and GFDL
URL:        http://www.gzip.org/
Source0:    ftp://alpha.gnu.org/gnu/gzip/gzip-%{version}.tar.xz
Patch1: gnulib.patch
Patch2: gzexe.patch
Requires:   /bin/mktemp
BuildRequires:  texinfo

%description
The gzip package contains the popular GNU gzip data compression
program. Gzipped files have a .gz extension.

Gzip should be installed on your system, because it is a
very commonly used data compression program.


%package -n zless
Summary:    file perusal filter for crt viewing of compressed text
License:    GPLv2
Group:      Applications/File
Requires:   %{name} = %{version}-%{release}
Requires:   /usr/bin/less

%description -n zless
Zless  is  a filter which allows examination of compressed or plain text files one
screenful at a time on a soft-copy terminal.  It is the equivalent of setting the
environment variable LESSOPEN to '|gzip -cdfq -- %s', and the environment variable
LESSMETACHARS to and then running less.  However,  enough people seem to think that
having the command zless available is important to be worth providing it.


%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}
Obsoletes: %{name}-docs

%description doc
Man and info pages for %{name}.


%prep
%setup -q -n %{name}-%{version}

%patch1 -p1 -b .gnulib
%patch2 -p1 -b .gzexe
autoreconf

%build
export CPPFLAGS="-DHAVE_LSTAT"

%configure --disable-static \
    --bindir=/usr/bin

make %{?jobs:-j%jobs}


%install
rm -rf %{buildroot}
%make_install

# we don't ship it, so let's remove it from ${RPM_BUILD_ROOT}
rm -f %{buildroot}%{_infodir}/dir
# uncompress is a part of ncompress package
rm -f %{buildroot}%{_bindir}/uncompress

mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}/%{_docdir}/%{name}-%{version} \
        AUTHORS ChangeLog ChangeLog-2007 NEWS README THANKS TODO

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/zcat
%{_bindir}/gzip
%{_bindir}/gunzip
%{_bindir}/zcmp
%{_bindir}/zegrep
%{_bindir}/zforce
%{_bindir}/znew
%{_bindir}/gzexe
%{_bindir}/zdiff
%{_bindir}/zfgrep
%{_bindir}/zgrep
%{_bindir}/zmore

%files -n zless
%defattr(-,root,root,-)
%{_bindir}/zless

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}
%{_mandir}/man1/*
%{_infodir}/gzip.info.gz
