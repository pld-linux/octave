Summary: GNU Octave -- a high-level language for numerical computations
Summary(pl): GNU Octave -- jêzyk programowania do obliczeñ numerycznych
Name: octave
Version: 2.0.14
Release: 1
Copyright: GPL
Group: Applications/Math
Group(pl): Aplikacje/Matematyczne
Source: ftp://ftp.che.wisc.edu/pub/octave/%{name}-%{version}.tar.bz2
URL: http://www.che.wisc.edu/octave/
BuildPrereq: libstdc++-devel
BuildPrereq: flex
BuildPrereq: bison
Requires: gnuplot
BuildRoot: /tmp/%{name}-%{version}-root


%description
GNU Octave is a high-level language, primarily intended for numerical
computations. It provides a convenient command line interface for
solving linear and nonlinear problems numerically, and for performing
other numerical experiments using a language that is mostly compatible
with Matlab. It may also be used as a batch-oriented language.

Octave has extensive tools for solving common numerical linear algebra
problems, finding the roots of nonlinear equations, integrating
ordinary functions, manipulating polynomials, and integrating ordinary
differential and differential-algebraic equations. It is easily
extensible and customizable via user-defined functions written in
Octave's own language, or using dynamically loaded modules written in
C++, C, Fortran, or other languages.

%description -l pl
GNU Octave jest jezykiem programowania wysokiego poziomu przeznaczonym 
g³ównie do obliczeñ numerycznych. Octave jest w du¿ym stopniu
kompatybilny z jezykiem Matlab. Pracowaæ mo¿na wprost z linii
poleceñ lub uruchamiaæ programy stworzone za pomoc± zewnêtrznego
edytora.

Ze wzglêdu na objêto¶æ dokumentacji w pakiecie binarnym znajduje
siê tylko jej czê¶æ (info, faq i manual(.html)) 
Ca³o¶æ mo¿na znale¼æ w pakiecie src.rpm

%changelog

* Fri Apr 30 1999 Rafa³ Kleger-Rudomin <klakier@pg.gda.pl>
- Adapt for PLD, update to Octave 2.0.14
 
* Thu Jun 11 1998 Andrew Veliath <andrewtv@usa.net>
- Add %attr, build as user.

* Mon Jun 1 1998 Andrew Veliath <andrewtv@usa.net>
- Add BuildRoot, installinfo, require gnuplot, description from
  Octave's web page, update to Octave 2.0.13.

- Adapt from existing spec file.

%prep

%setup -q

%build
CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" ./configure \
     --prefix=/usr \
     --with-g77 \
     --enable-dl \
     --enable-shared \
     --enable-rpath \
     --enable-lite-kernel
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install
gzip -9nf $RPM_BUILD_ROOT/usr/info/%{name}.info*

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig
/sbin/install-info /usr/info/%{name}.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
   /sbin/install-info --delete /usr/info/%{name}.info.gz /etc/info-dir
fi

%postun -p /sbin/ldconfig

%files

%defattr(644, root, root, 755)
%attr(755, root, root) /usr/bin/*
/usr/include/%{name}-%{version}
/usr/info/%{name}.info*
/usr/lib/%{name}-%{version}
%attr(755, root, root) /usr/libexec/%{name}
/usr/man/man1/%{name}.1
/usr/share/%{name}
%doc BUGS COPYING NEWS* PROJECTS README README.Linux ChangeLog* ROADMAP SENDING-PATCHES THANKS
%doc doc/faq emacs examples doc/interpreter/*.html
    
