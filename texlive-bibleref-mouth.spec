%global tl_name bibleref-mouth
%global tl_revision 25527

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Consistent formatting of Bible references
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bibleref-mouth
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-mouth.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-mouth.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-mouth.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows Bible references to be formatted in a consistent way.
It is similar to the bibleref package, except that the formatting macros
are all purely expandable -- that is, they are all implemented in TeX's
mouth. This means that they can be used in any expandable context, such
as an argument to a \url command.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bibleref-mouth
%dir %{_datadir}/texmf-dist/source/latex/bibleref-mouth
%dir %{_datadir}/texmf-dist/tex/latex/bibleref-mouth
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-mouth/README
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-mouth/bibleref-mouth.pdf
%doc %{_datadir}/texmf-dist/source/latex/bibleref-mouth/bibleref-mouth.dtx
%doc %{_datadir}/texmf-dist/source/latex/bibleref-mouth/bibleref-mouth.ins
%{_datadir}/texmf-dist/tex/latex/bibleref-mouth/bibleref-mouth.sty
